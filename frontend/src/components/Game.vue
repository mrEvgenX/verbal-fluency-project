<template>
    <div class="container game">
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
            </div>
        </div>
    </div>
</template>

<script>
import WordsList from './game_parts/WordsList.vue'
import Timer from './game_parts/Timer.vue'

export default {
    name: 'Game',
    props: ['initialTime', 'prefix'],
    data() {
        return {
            suffix: '',
            typedWords: [],
            timer: null,
            secondsLeft: this.initialTime,
            score: 0
        }
    },
    methods: {
        handleInput(event) {
            let newSuffix = event.target.value.substring(this.prefix.length);
            this.suffix = newSuffix;
        },
        addTypedWord() {
            let notTypedBefore = !this.typedWords.includes(this.word);
            if(notTypedBefore) {
                fetch('http://localhost:5050/valid?word=' + this.word).then(
                    response => {
                        return response.json();
                    }
                ).then(
                    data => {
                        let valid = data.result;
                        if (valid) {
                            this.typedWords.push(this.word);
                            this.suffix = "";
                            this.score += 1;
                        }
                    }
                )
            }
        },
        setTimer() {
            this.clearTimer()
            this.timer = setInterval(
                () => {
                    if(this.secondsLeft > 0) {
                        this.secondsLeft--;
                    } else {
                        this.clearTimer();
                        this.$emit('game-over', this.score);
                    }
                },
                1000
            )
        },
        clearTimer() {
            if(this.timer) {
                clearInterval(this.timer);
            }
        }
    },
    mounted() {
        this.setTimer();
    },
    computed: {
        word() {
            return this.prefix + this.suffix
        }
    },
    directives: {
        focus: {
            inserted: function (el) {
                el.focus()
            }
        }
    },
    components: {
        WordsList,
        Timer
    }
}
</script>