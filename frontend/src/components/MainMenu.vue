<template>
    <div class="container h-100 main-menu">
        <div class="row h-100 align-items-center">
            <div class="col align-text-center">
                <button class="btn btn-primary" @click="startGame">Начать игру</button>
            </div>
        </div>
        
    </div>
</template>

<script>

export default {
    name: 'MainMenu',
    methods: {
        startGame() {
            this.$emit('start-game');
        }
    }
}
</script>
