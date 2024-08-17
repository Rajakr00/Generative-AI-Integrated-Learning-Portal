<template>
    <div class="chatbotContainer">
        <img src="../assets/robot.png" class="chatbotIcon" v-on:click="redirectChatbot" />
    </div>
    <footer class="sticky-bottom d-flex align-items-center justify-content-center mt-auto">
        <hr>
        <center>Team12 &copy; 2024</center>    
    </footer>
</template>

<script>
export default {
  name: 'Footer',
  props: ['footnote'],
  methods: {
    redirectChatbot() {
      //console.log('Redirecting to Chatbot:')
      this.$router.push({
        path: '/Chatbot',
        
      })
    },

  }
}
</script>

<style>
.chatbotIcon{
  height: 100px;
  padding: 10px;
}
.chatbotContainer{
  height: fit-content;
  width: fit-content;
  border-radius: 11cm;
  background-color: #8d493a;
  float:right;
  position: absolute; 
  top: 80%;
  right: 10%; 
  /* z-index: 1000; */
}
.chatbotIcon:hover{
  cursor: pointer;
}
.chatbotContainer:hover{
  opacity: 95%;
  border: 2px solid #d0b8a8;
}

</style>