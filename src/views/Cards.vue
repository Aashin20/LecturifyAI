<template>
  <div class="flashcard-stack">
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
    <h1 class="title">Flashcards curated for you</h1>

    <div v-for="(card, index) in cards" :key="card[0]" class="flashcard"
      :class="{ flipped: flippedCardIndex === index }" @click="toggleFlip(index)" :style="{
        transform: `translateY(${index * 10}px)`,
        zIndex: cards.length - index
      }">
      <button class="delete-btn" @click.stop="removeCard(index)">X</button>
      <div class="inner">
        <div class="front">
          <p>{{ card[1] }}</p>
        </div>
        <div class="back">
          <p>{{ card[2] }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useMainStore } from '@/stores/main';
import { storeToRefs } from 'pinia';


const main = useMainStore()
const { flashcardData } = storeToRefs(main)
const { getFlashCards } = main;

const cards = ref([]);
cards.value = flashcardData.value;
onMounted(getFlashCards)



const flippedCardIndex = ref(null);

const toggleFlip = (index) => {
  flippedCardIndex.value = flippedCardIndex.value === index ? null : index;
};

const removeCard = (index) => {
  cards.value.splice(index, 1);
};
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 3.5rem;
}

.title {
  font-weight: 600;
  margin-bottom: 1rem;
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
  margin-right: -1.9rem;
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

.flashcard-stack {
  font-family: Poppins;
  position: relative;
  width: 93%;
  height: 30rem;
  padding: 1rem 0.8rem;
  perspective: 1000px;
  /* Perspective to create 3D effect */
}

.flashcard {
  position: absolute;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  /* Ensure child elements are rendered in 3D space */
  transition: transform 0.6s ease-in-out;
  cursor: pointer;
}

.flashcard.flipped .inner {
  transform: rotateY(180deg);
  /* Flip the card when flipped class is applied */
}

.inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.6s ease-in-out;
  transform-style: preserve-3d;
}

.front,
.back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  /* Hide backface of the element when facing away */
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1.5rem;
  font-size: 1rem;
  color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.front {
  background-color: #5EB670;
  text-align: center;
  padding: 2rem 2rem;
  color: white;
  font-family: Poppins;
  font-weight: 600;
}

.back {
  background-color: #F4F4F4;
  color: #5EB670;
  padding: 2rem 2rem;
  font-weight: 400;
  transform: rotateY(180deg);
  /* Initially hide the back face */
}

.delete-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(255, 255, 255, 0.7);
  border: none;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  cursor: pointer;
  color: #333;
  z-index: 1;
  /* Ensure it stays above the card content */
}
</style>