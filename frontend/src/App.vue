<template>
    <div id="app">
        <component 
            :is="currentScreen" 
            @start-game="startGame"
            initialTime="30"
            :prefix="prefix"
            @game-over="gameOver"
            :score="score"></component>
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
            prefix: '',
            score: 0
        }
    },
    methods: {
        startGame() {
            fetch('http://localhost:5050/prefix').then(
                    response => {
                        return response.json();
                    }
                ).then(
                    data => {
                        this.prefix = data.result;
                        this.currentScreen = Game;
                    }
                )
        },
        gameOver(score) {
            this.score = score;
            this.currentScreen = Score;
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
