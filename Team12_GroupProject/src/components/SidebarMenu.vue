<template>


  <div class="sidebarmenu">

    <!--
    <div class="toggleButtonDiv">
      <img @click="toggleSidebar" class="toggleBtn" src="@/assets/menu.png" alt="Toggle Sidebar" />
    </div>

    <div :class="['sidebar', { 'sidebar-closed': !isSidebarOpen }]">
    -->

    <div class="offcanvas offcanvas-start show" tabindex="-1" id="offcanvas" aria-labelledby="offcanvasLabel" style="background-color:#f8ede3;">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasLabel">Lectures</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <div class="sidebar-header">
        <h2>{{ name }}</h2>
      </div>
      <ul class="sidebar-menu list-group">
        <li v-for="(week, index) in weeks" :key="index" class="menu-item list-group-item btn" data-bs-toggle="collapse" :data-bs-target="'#collapseExample' + index" aria-expanded="false" :aria-controls="'collapseExample' + index">
          {{ week.week }}
          <div class="collapse" :id="'collapseExample' + index">
          <ul class="list-group bg-secondary">
            <li v-for="(url, idx) in week.urls" :key="idx" class="list-unstyled">
              <a href="#" @click.prevent="handleTopicClick(url)" class="list-group-item" data-bs-dismiss="offcanvas"> Topic {{ idx + 1 }}</a>
            </li>
          </ul>
          </div>
        </li>
      </ul>
    </div>
  </div>
</div>

      



</template>

<script>
export default {
  name: 'SidebarMenu',
  props: {
    name: {
      type: String,
      required: false
    },
    weeks: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      isSidebarOpen: true
    }
  },
  methods: {
    handleTopicClick(url) {
      this.$emit('selectTopic', url)
    },
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen
    }
  }
}
</script>

<style>
@media (min-width: 768px) {
  .offcanvas {
    width: 25%;
  }
}

.list-unstyled:hover{
  background-color: rgb(141 74 58);
  }
</style>
