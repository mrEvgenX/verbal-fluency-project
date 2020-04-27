<template>
    <div class="container score">
        <p>Итоговый счет: {{score}}</p>
        <button class="btn btn-primary" @click="startGame">Заново</button>
    </div>
</template>

<script>

export default {
    name: 'Score',
    props: ['score'],
    methods: {
        startGame() {
            this.$emit('start-game');
        }
    }
}
</script>