<template>
    <div id="app">
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
import MainMenu from './components/MainMenu.vue'
import Game from './components/Game.vue'
import Score from './components/Score.vue'

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

<style>
html, body {
    height: 100%;
}
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    height: 100%;
}
</style>
