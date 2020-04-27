<template>
    <div class="timer">
        <p>{{minutes()}}:{{seconds()}}</p>
    </div>
</template>

<script>

export default {
    name: 'Timer',
    props: ['secondsLeft'],
    methods: {
        minutes() {
            return Math.floor(this.secondsLeft / 60);
        },
        seconds() {
            return this.secondsLeft % 60;
        }
    }
}
</script>