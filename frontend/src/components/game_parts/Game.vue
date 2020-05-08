<template>
    <div class="row">
        <div class="col-9">
            <input
                v-focus
                class="form-control"
                :class="{'is-invalid': lastWordWasInvalid}"
                :value="word" type="text"
                @input="handleInput"
                @keyup.enter="addTypedWord" />
            <Timer 
                :totalSeconds = "totalSeconds"
                :secondsLeftForEveryStage="secondsLeftForEveryStage" />
            <WordsList :typedWords="typedWords" />
        </div>
        <div class="col-3">
            <p>{{score}}</p>
        </div>
    </div>
</template>

<script>
import WordsList from './WordsList.vue'
import Timer from './Timer.vue'

export default {
    name: 'Game',
    props: ['basicPrefixLength', 'roundStagesDurations'],
    data() {
        return {
            prefixes: [],
            currentPrefix: '',
            suffix: '',
            lastWordWasInvalid: false,
            inputValidTimer: null,
            typedWords: [],
            timer: null,
            currentRound: 0,
            currentStage: 0,
            secondsLeftForEveryStage: [],
            totalSeconds: 0,
            score: 0
        }
    },
    methods: {
        handleInput(event) {
            let newSuffix = event.target.value.substring(this.currentPrefix.length);
            this.suffix = newSuffix;
        },
        addTypedWord() {
            let notTypedBefore = !this.typedWords.includes(this.word);
            if(notTypedBefore) {
                fetch('http://localhost:5050/valid?word=' + this.word)
                    .then(response => response.json())
                    .then(data => {
                        let valid = data.result;
                        this.lastWordWasInvalid = !valid;
                        if (valid) {
                            this.typedWords.push(this.word);
                            switch (this.word.length) {
                                case 1:
                                case 2:
                                case 3:
                                    this.score += 1;
                                    break;
                                case 4:
                                    this.score += 2;
                                    break;
                                case 5:
                                    this.score += 3;
                                    break;
                                case 6:
                                    this.score += 4;
                                    break;
                                case 7:
                                    this.score += 5;
                                    break;
                                default:
                                    this.score += 6;
                                    break;
                            }
                        } else {
                            if (this.inputValidTimer) {
                                clearTimeout(this.inputValidTimer);
                            }
                            this.inputValidTimer = setTimeout(() => {
                                this.lastWordWasInvalid = false;
                            }, 1000);
                        }
                        this.suffix = "";
                    })
            } else {
                this.lastWordWasInvalid = true;
                if (this.inputValidTimer) {
                    clearTimeout(this.inputValidTimer);
                }
                this.inputValidTimer = setTimeout(() => {
                    this.lastWordWasInvalid = false;
                }, 500);
            }
        },
        async getPrefix(prefixLength) {
            let url = 'http://localhost:5050/prefix?prefix_length=' + prefixLength;
            let response = await fetch(url);
            let data = await response.json();
            return data.result;
        },
        async fillPrefixes() {
            let basePrefix = await this.getPrefix(this.basicPrefixLength);
            this.roundStagesDurations.forEach((item, index) => {
                this.prefixes.push(basePrefix.substring(0, basePrefix.length - index));
            })
        },
        async init() {
            this.clearTimer();
            this.roundStagesDurations.forEach((item) => {
                this.totalSeconds += item;
            })
            this.secondsLeftForEveryStage = [...this.roundStagesDurations];
            this.currentStage = 0;
            await this.fillPrefixes();
            this.applyStage();
        },
        setTimer() {
            this.timer = setInterval(
                () => {
                    let currentSecondsMinusOne = this.secondsLeftForEveryStage[this.currentStage] - 1;
                    this.$set(this.secondsLeftForEveryStage, this.currentStage, currentSecondsMinusOne);
                    if (currentSecondsMinusOne <= 0) {
                        this.currentStage++;
                        let totalStages = this.roundStagesDurations.length;
                        if(this.currentStage >= totalStages) {
                            this.clearTimer();
                            this.$emit('round-finished', this.score);
                        } else {
                            this.applyStage();
                        }
                    }
                },
                1000
            );
        },
        applyStage() {
            if (this.currentStage > 0 && this.suffix.length > 0) {
                let lastLetterOfPrevPrefix = this.currentPrefix[this.currentPrefix.length-1];
                this.suffix = lastLetterOfPrevPrefix + this.suffix;
            }
            this.currentPrefix = this.prefixes[this.currentStage];
        },
        clearTimer() {
            if(this.timer) {
                clearInterval(this.timer);
            }
        }
    },
    async mounted() {
        await this.init()
        this.setTimer();
    },
    computed: {
        word() {
            return this.currentPrefix + this.suffix;
        }
    },
    directives: {
        focus: {
            inserted: function (el) {
                el.focus();
            }
        }
    },
    components: {
        WordsList,
        Timer
    }
}
</script>