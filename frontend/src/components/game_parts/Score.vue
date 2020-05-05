<template>
    <div class="container score">
        <p>Счет: {{score}}</p>
        <button class="btn btn-primary" @click="nextRound">Далее</button>
    </div>
</template>

<script>

export default {
    name: 'Score',
    props: ['score'],
    methods: {
        nextRound() {
            this.$emit('next-round');
        }
    }
}
</script>