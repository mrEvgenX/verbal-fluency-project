<template>
    <div id="app">
        <ul>
            <li><router-link to='/'>Главная</router-link></li>
            <li><router-link to='/profile/total_score'>Общий счет</router-link></li>
            <li><router-link to='/profile'>Профиль</router-link></li>
            <li><router-link to='/login'>Вход</router-link></li>
            <li><router-link to='/register'>Регистрация</router-link></li>
        </ul>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: 'App',
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
