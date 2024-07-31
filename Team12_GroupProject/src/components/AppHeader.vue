<template>
 <header class="sticky-top">
<div class="row p-1">
<span class="d-flex col-4 text-start">


<a v-if="currentUser && isTitleMatch" class="btn btn-primary p-1" style="background-color: #f8ede3;color: #8d4a3a;border: none;" data-bs-toggle="offcanvas" href="#offcanvas" role="button" aria-controls="offcanvasExample">
  <i v-if="isMobile" class='bx bx-book-open bx-sm'></i><p class="m-0" v-else >lectures</p>
</a>
<p v-if="currentUser" class="m-0 ms-2 align-self-center">Hi, {{ currentUser.name }}</p>


</span>
  <span class="col-4 align-self-center">
    <a @click.prevent="goToDashboard">IITM BS</a>
  </span>
  <span class="col-4 text-end align-self-center">
    <a v-if="currentUser" @click.prevent="logout">log out</a>
  </span>
</div>
</header>
</template>

<script>
export default {

  name: 'Header',
  props: ['heading'],
  data(){
  return{
    screenWidth: window.innerWidth,
  };
  },
  methods:{

   handleResize() {
      this.screenWidth = window.innerWidth;
    },

  goToDashboard(){
    const user_id = this.$store.state.current_user.id;
    this.$router.push({ path: '/studentDashboard', query: { user_id } })
  },
  logout(){
    this.$store.commit('setCurrentUser', null)
    this.$router.push({ path: '/'})
  },
  

  },
 computed: {

    isMobile() {
    console.log(this.screenWidth);
      return this.screenWidth < 768;

    },

  isTitleMatch() {
      console.log(this.$route.meta.pageName)
      return this.$route.meta.pageName === "coursePage";

    },

  currentUser() {
    const current_user = this.$store.state.current_user;
    return current_user ? current_user : null;
  },

},
created() {
    window.addEventListener('resize', this.handleResize);
  },
  destroyed() {
    window.removeEventListener('resize', this.handleResize);
  }
}
</script>

<style></style>
