<template>
    <div class="timer">
        <div class="progress">
            <div class="progress-bar emptiness" role="progressbar" :style="{width: secondsEmptiness() + '%'}"></div>
            
            <div 
                class="progress-bar progress-stage-1" 
                role="progressbar" 
                :style="{width: secondsStage1() + '%'}"></div>

            <div 
                class="progress-bar progress-stage-2" 
                role="progressbar" 
                :style="{width: secondsStage2() + '%'}"></div>

            <div 
                class="progress-bar progress-stage-3" 
                role="progressbar" 
                :style="{width: secondsStage3() + '%'}"></div>

            <div 
                class="progress-bar progress-stage-2" 
                role="progressbar" 
                :style="{width: secondsStage2() + '%'}"></div>

            <div 
                class="progress-bar progress-stage-1" 
                role="progressbar" 
                :style="{width: secondsStage1() + '%'}"></div>

            <div class="progress-bar emptiness" role="progressbar" :style="{width: secondsEmptiness() + '%'}"></div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Timer',
    props: ['totalSeconds', 'secondsLeftForEveryStage'],
    data() {
        return {
            secs: [5,5,5]
        }
    },
    methods: {
        secondsStage1() {
            let result = 0;
            if (this.secondsLeftForEveryStage.length > 0) {
                result =this.secondsLeftForEveryStage[0];
            }
            return result/this.totalSeconds*100/2;
        },
        secondsStage2() {
            let result = 0;
            if (this.secondsLeftForEveryStage.length >= 2) {
                result =this.secondsLeftForEveryStage[1];
            }
            return result/this.totalSeconds*100/2;
        },
        secondsStage3() {
            let result = 0;
            if (this.secondsLeftForEveryStage.length >= 3) {
                result = this.secondsLeftForEveryStage[2];
            }
            return result/this.totalSeconds*100;
        },
        secondsEmptiness() {
            let result = this.totalSeconds;
            this.secondsLeftForEveryStage.forEach((item) => {
                result -= item;
            })
            return result/this.totalSeconds*100/2;
        },
        secondsLeft() {
            let result = 0;
            this.secondsLeftForEveryStage.forEach((item) => {
                result += item;
            })
            return result;
        },
        minutes() {
            return Math.floor(this.secondsLeft() / 60);
        },
        seconds() {
            return this.secondsLeft() % 60;
        }
    }
}
</script>

<style>
.progress {
    margin-top: 5px;
}

.emptiness {
    background-color: white;
}

.progress-stage-1 {
    background-color: green;
}

.progress-stage-2 {
    background-color: yellow;
}

.progress-stage-3 {
    background-color: red;
}
</style>