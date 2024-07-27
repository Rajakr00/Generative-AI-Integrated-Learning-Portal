<template>
  <div class="sidebarmenu">
    <div class="toggleButtonDiv">
      <img @click="toggleSidebar" class="toggleBtn" src="@/assets/menu.png" alt="Toggle Sidebar" />
    </div>
    <div :class="['sidebar', { 'sidebar-closed': !isSidebarOpen }]">
      <div class="sidebar-header">
        <h2>{{ name }}</h2>
      </div>
      <ul class="sidebar-menu">
        <li v-for="(week, index) in weeks" :key="index" class="menu-item">
          {{ week.week }}
          <ul>
            <li v-for="(url, idx) in week.urls" :key="idx">
              <a href="#" @click.prevent="handleTopicClick(url)"> Topic {{ idx + 1 }}</a>
            </li>
          </ul>
        </li>
      </ul>
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
.sidebarmenu {
  width: 100px;
  height: 100vh;
  background-color: #8d493a;
  color: black;
  display: flex;
  flex-direction: column;
  position: fixed;
  left: 0;
  top: 0;
  transition: transform 0.3s ease;
  overflow: hidden;
  z-index: 1000;
}

.sidebar {
  width: 200px;
  height: 100vh;
  padding-top: 70px;
  background-color: #8d493a;
  color: #f8ede3;
  display: flex;
  flex-direction: column;
  position: fixed;
  left: 0;
  top: 0;
  transition: transform 0.3s ease;
  overflow: hidden; /* Hide overflow to prevent scrollbars */
  z-index: 1000; /* Ensure the sidebar is on top */
}

.sidebar-header {
  padding: 20px;
  text-align: center;
  margin-left: 10px;
  border-bottom: 1px solid #9f9999;
  font-family: 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  font-weight: bolder;
  font-size: 20px;
  color: #f8ede3;
}

.sidebar-menu {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu-item {
  padding: 15px;
  padding-left: 20px;
  margin-left: 10px;
  border-bottom: 1px solid #9f9999;
  font-family: 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  font-weight: bolder;
  font-size: 20px;
  color: #f8ede3;
}

.sub-topic {
  padding: 5px;
  padding-left: 15px;
  font-family: 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  font-weight: bolder;
  font-size: 15px;
  color: #f8ede3;
}

.sub-topic :hover {
  background-color: #833006;
  cursor: pointer;
}

.toggleButtonDiv {
  margin: 10px;
}

.toggleBtn {
  width: 50px;
  height: 50px;
  position: absolute;
  top: 20px;
  left: 100%;
  margin-left: -80px;
  /* background-color: #a00e0e; */
  /* color: #fff; */
  border: none;
  padding: 10px;
  cursor: pointer;
  z-index: 1001;
}

.sidebar-closed {
  transform: translateX(-100%);
}

.sidebar-closed .menu-item span {
  display: none; /* Hide text when sidebar is closed */
}
</style>
