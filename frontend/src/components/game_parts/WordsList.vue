<template>
    <div class="words-list">
        <div v-for="(bucket, index) in wordBuckets" :key="index">
            <p>{{bucket[0]}}</p>
            <ul :style="{'text-color': true}">
                <li v-for="(word, index) in bucket[1]" :key="index">{{word}}</li>
            </ul>
        </div>
    </div>
</template>

<script>

export default {
    name: 'WordsList',
    props: ['typedWords'],
    computed: {
        wordBuckets() {
            let result = new Map();
            for(let word of this.typedWords) {
                if(!result.has(word.length)) {
                    result.set(word.length, []);
                }
                result.get(word.length).push(word);
            }
            return result;
        }
    }
}
</script>