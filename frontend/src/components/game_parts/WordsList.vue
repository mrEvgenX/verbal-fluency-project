<template>
    <div class="words-list">
        <p>{{joinedAll}}</p>
    </div>
</template>

<script>

export default {
    name: 'WordsList',
    props: ['typedWords'],
    computed: {
        joinedAll() {
            return this.typedWords.join(' ')
        }
    }
}
</script>