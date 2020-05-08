<template>
    <div class="container score">
        <p>Итоговый счет: {{score}}</p>
        <button class="btn btn-primary" @click="toMainMenu">Заново</button>
    </div>
</template>

<script>

export default {
    name: 'Score',
    props: ['score'],
    methods: {
        toMainMenu() {
            this.$emit('to-main-menu');
        }
    }
}
</script>