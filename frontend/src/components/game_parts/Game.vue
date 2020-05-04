<template>
    <div class="row">
        <div class="col-9">
            <input
                v-focus
                class="form-control"
                :value="word" type="text"
                @input="handleInput"
                @keyup.enter="addTypedWord" />
            <WordsList :typedWords="typedWords" />
        </div>
        <div class="col-3">
            <Timer :secondsLeft="secondsLeft" />
            <p>{{score}}</p>
            {{roundStagesDurations}}
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
            typedWords: [],
            timer: null,
            currentRound: 0,
            secondsLeft: 0,
            score: 0,
            currentStage: 0,
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
                    .then(response => {
                        return response.json();
                    })
                    .then(data => {
                        let valid = data.result;
                        if (valid) {
                            this.typedWords.push(this.word);
                            this.suffix = "";
                            this.score += 1;
                        }
                    })
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
        applyStage() {
            this.currentPrefix = this.prefixes[this.currentStage];
            this.suffix = '';
        },
        async setTimer() {
            // init
            this.secondsLeft = 0;
            this.roundStagesDurations.forEach((item) => {
                this.secondsLeft += item;
            })
            this.currentStage = 0;
            this.clearTimer();
            await this.fillPrefixes();
            this.applyStage();
            this.timer = setInterval(
                () => {
                    let totalStages = this.roundStagesDurations.length;
                    if(this.secondsLeft > 0) {
                        this.secondsLeft--;
                        this.roundStagesDurations[this.currentStage]--;
                        if (this.roundStagesDurations[this.currentStage] <= 0) {
                            this.currentStage++;
                            if (this.currentStage < totalStages) {
                                this.applyStage();
                            } else {
                                this.clearTimer();
                                this.$emit('round-finished');
                            }
                        }
                    } else {
                        this.clearTimer();
                        this.$emit('round-finished');
                    }
                },
                1000
            );
        },
        clearTimer() {
            if(this.timer) {
                clearInterval(this.timer);
            }
        }
    },
    mounted() {
        this.setTimer().then(() => {});
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