<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="greetings">
    <h1>Team12 Project</h1>
  </div>
  <nav>
    <a href="/html/">StudentLogin</a> |
    <a href="/css/">AdminLogin</a>
  </nav>

  <form>
    <ul>
      <input type="text" placeholder="Username" required>
    </ul>
    <ul>
      <input type="password" required>
    </ul>
    <ul>
      <button>Login</button>
    </ul>
  </form>

</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
