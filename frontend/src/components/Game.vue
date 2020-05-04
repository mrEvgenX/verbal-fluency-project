<template>
    <div class="container game">
        <component 
            :is="state" 
            :basicPrefixLength="basicPrefixLength"
            :roundStagesDurations="roundStagesDurations"
            @round-finished="showSubScore"></component>
    </div>
</template>

<script>
import Game from './game_parts/Game.vue'
import Score from './game_parts/Score.vue'

export default {
    name: 'Game',
    props: ['rounds'],
    data() {
        return {
            state: null,
            currentRound: 0,
            basicPrefixLength: null,
            roundStagesDurations: null,
            score: 0,
        }
    },
    methods: {
        startGame() {
            this.basicPrefixLength=this.rounds[this.currentRound][0];
            this.roundStagesDurations=this.rounds[this.currentRound][1];
            this.state = Game;
        },
        showSubScore() {
            this.state = Score;
        }
    },
    mounted() {
        this.startGame();
    },
    components: {
        Game,
        Score
    }
}
</script>