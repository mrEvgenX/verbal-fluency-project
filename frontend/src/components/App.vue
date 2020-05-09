<template>
    <div id='main-app'>
        <component 
            :is="currentScreen" 
            @start-game="startGame"
            :rounds="rounds"
            @game-over="gameOver"
            :score="score"
            @to-main-menu="toMainMenu"></component>
    </div>
</template>

<script>
import MainMenu from './MainMenu.vue'
import Game from './Game.vue'
import Score from './Score.vue'

export default {
    name: 'App',
    data() {
        return {
            currentScreen: MainMenu,
            score: 0,
            rounds: [
                [2, [30]],
                [3, [15, 15]],
                [4, [15, 15, 15]]
            ]
        }
    },
    methods: {
        startGame() {
            this.currentScreen = Game;
        },
        gameOver(score) {
            this.score = score;
            this.currentScreen = Score;
        },
        toMainMenu() {
            this.currentScreen = MainMenu;
        }
    },
    components: {
        MainMenu,
        Game,
        Score
    }
}
</script>

<style scoped>
#main-app {
    height: 100%
}
</style>
