<template>
  <SidebarMenu :name="course_name" :weeks="weeks_no" @selectTopic="selectTopic" />
  <VideoPlayer :videoUrl="selectedVideoUrl" />
  <div class="body">
    <p>
      Youtube Video URL :
      <span>{{ selectedVideoUrl }}</span>
      <button @click="copyToClipboard(selectedVideoUrl)">Copy Link</button>
    </p>
  </div>
</template>

<script>
import SidebarMenu from './SidebarMenu.vue'
import VideoPlayer from './VideoPlayer.vue'
export default {
  name: 'CoursePage',
  components: {
    SidebarMenu,
    VideoPlayer
  },
  created() {
    this.getCoursesDetails()
  },
  data() {
    return {
      user_id: this.$route.query.user_id,
      course_id: this.$route.query.course_id,
      message: null,
      details: [],
      course_name: null,
      weeks_no: [],
      selectedVideoUrl: ''
    }
  },
  mounted() {
    this.setInitialVideo()
  },
  methods: {
    async getCoursesDetails() {
      const response = await fetch(
        `http://127.0.0.1:5000//api/coursePage?user_id=${this.user_id}&course_id=${this.course_id}`,
        {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        }
      )
      const data = await response.json()
      if (response.ok) {
        this.course_name = data['course_name']
        this.details = data['details']
        this.weeks_no = Object.entries(this.details).map(([weekNumber, urls]) => ({
          week: `Week ${weekNumber}`,
          urls
        }))
        console.log(this.weeks_no)
        this.setInitialVideo()
      } else this.message = data['message']
    },
    setInitialVideo() {
      if (this.weeks_no.length > 0 && this.weeks_no[0].urls.length > 0) {
        this.selectedVideoUrl = this.convertToEmbedUrl(this.weeks_no[0].urls[0])
      }
    },

    selectTopic(url) {
      this.selectedVideoUrl = this.convertToEmbedUrl(url)
    },

    convertToEmbedUrl(url) {
      const videoId = url.split('/').pop().split('?')[0]
      return `https://www.youtube.com/embed/${videoId}`
    },
    copyToClipboard() {
      navigator.clipboard.writeText(this.selectedVideoUrl).then(() => {
        alert('Link copied to clipboard')
      })
    }
  }
}
</script>

<style scoped>
.body {
  padding-left: 200px;
}
</style>
