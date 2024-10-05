<template>
    <div class="wrapper">
        <div class="header" @click="$router.push('/')">
            <span class="left">
                <img src="../assets/logo.png" alt="logo" class="logo">
                <span class="f-row">
                    <h1 class="name">Lecturify</h1>
                    <h2 class="motto">Education Unlocked</h2>
                </span>
            </span>
            <img src="../assets/avatar.png" alt="avatar" class="avatar">
        </div>

        <div class="flex-wrapper">
            <div class="completion-level">
                <div class="completed-level"></div>
            </div>
        <span>
            <h1 class="question-no">Q1:</h1>
            <h2 class="question">The ability of one class to acquire methods and attributes of another class is called?</h2>
        </span>    

        <span class="bottom-content">
            <div v-for="(choice, index) in choices" :key="index">
      <button class="box"
        :class="{
          'choice-btn': true,
          'correct': choice.correct && choice.selected,
          'incorrect': !choice.correct && choice.selected,
        }"
        @click="selectChoice(index)"
      >
        {{ choice.text }}
      </button>
    </div>
            <div class="next" v-if="showActionButton">CONTINUE</div>
        </span>
        </div>
        
    </div>
</template>

<script setup>
import { ref } from 'vue';

// Define the list of choices
const choices = ref([
  { text: 'James Van Dym', correct: false, selected: false },
  { text: 'Stan Lee', correct: false, selected: false },
  { text: 'Sundar Pichai', correct: false, selected: false },
  { text: 'Guido Van Rossum', correct: true, selected: false },
]);

let showActionButton = ref(false)

// Function to handle choice selection
const selectChoice = (index) => {
  // Set all choices to unselected
  choices.value.forEach(choice => choice.selected = false);
    showActionButton.value = true;
  // Mark the clicked choice as selected
  choices.value[index].selected = true;
};
</script>

<style scoped>
.correct {
    border: #5EB670 solid 0.1px;
    background-color: rgba(94,182,112,0.1) !important;
}

.incorrect {
    border: #E83A3C solid 0.1px;
    background-color: rgba(232,58,60,0.1) !important;
}

.completion-level {
    height: 0.8rem;
    width: 93%;
    border-radius: 0.5rem;
    background-color: #EEEEEE;
    margin-left: 0.8rem;
    margin-bottom: 2rem;
}

.completed-level {
    height: inherit;
    width: 30%;
    background-color: #5EB670;
    border-radius: 0.5rem 0 0 0.5rem;
    animation-name: width-increase;
    animation-duration: 1s;
}

@keyframes width-increase {
    from {
        width:15%;
    }
    to {
        width:30%;
    }
}

.next {
    height: 4rem;
    width: 100%;
    position: fixed;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #5EB670;
    font-size: 1rem;
    font-weight: 600;
    bottom: 0;
    color: #ffffff;
    opacity: 1;
	animation-name: fadeInOpacity;
	animation-iteration-count: 1;
	animation-timing-function: ease-in;
	animation-duration: 0.6s;
}

@keyframes fadeInOpacity {
	0% {
		opacity: 0;
	}
	100% {
		opacity: 1;
	}
}

.box {
    margin-bottom: 0.4rem;
    border: 0.1px solid #A1A1A1;
    border-radius: 0.5rem;
    padding: 1.2rem 0rem;
    margin-left: 0.8rem;
    color: black;
    width: 100%;
    text-align: center;
    bottom: 1rem;
    font-size: 0.9rem;
    background-color: #fff;
}

.bottom-content {
    display: flex;
    flex-direction: column;
    position: absolute;
    bottom: 1rem;
    min-width: 92%;
    padding-bottom: 3.5rem;
}

.wrapper {
    height: 100%;
    padding: 1rem 0rem;
    font-family: Poppins;
}

.header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 2.5rem;
    padding: 0rem 0.8rem;
}

.left {
    display: flex;
    align-items: center;
}

.f-row {
    display: flex;
    flex-direction: column;
}

.logo {
    height: 3.3rem;
    width: 3.3rem;
    max-height: 3.3rem;
    max-width: 3.3rem;
    margin-right: 0.5rem;
}

.avatar {
    height: 3.3rem;
    width: 3.3rem;
    max-height: 3.3rem;
    max-width: 3.3rem;
}

.name {
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 0.3rem;
}

.motto {
    font-weight: 400;
    font-style: italic;
    font-size: 0.7rem;
}

.question-no {
    margin-left: 0.8rem;
    font-weight: 600;
    font-size: 0.8rem;
    margin-bottom: 0.6rem;
}

.question {
    margin-left: 0.8rem;
    font-weight: 300;
    font-size: 1rem;
    width: 80%;
    line-height: 1.8rem;
}
</style>