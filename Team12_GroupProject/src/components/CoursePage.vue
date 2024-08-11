<template>

  
  <SidebarMenu :name="course_name" :weeks="weeks_no" @selectTopic="selectTopic" /> 


  <div class="row m-1" v-if="checkSummary">
    <div class="col-md-7 p-0">
      <VideoPlayer :videoUrl="selectedVideoUrl" />
    </div>
    <div class="col md-5 p-1">

    <Chatbot :chatBotState="summary" :clearHistory="clearHistory" @closeChatBot="closeChatBot"/>
  
<!--
      <div class="card vh-100 m-2">
      <div class="card-header d-flex row">
        <div class="d-flex justify-content-between col align-self-center">
          <span class="fs-6 align-self-center">Summary</span>
          <span>
            <a class="btn btn-primary w-auto text-end col" @click="getSummary"><i class='bx bx-refresh bx-sm'></i></a></span>
        </div>
        <div class="col"></div>
  
        <div class="col d-flex justify-content-end ">
          <button class="btn btn-secondary" @click="closeSummary"><i class='bx bx-x bx-sm'></i></button>
        </div>
      </div>
      <div class="card-body overflow-scroll" v-html="summary">
      </div>

      </div>
-->    
    </div>

  </div>
  <div class="row m-1" v-else>
    <div class="row">
      <VideoPlayer :videoUrl="selectedVideoUrl" />
    </div>
    <div class="row">
    <div class="col"></div>
    <div class="col d-flex justify-content-center">
    <button class="btn btn-primary" @click="getSummary">Get Summary</button>
    </div>
    <div class="col"></div>
    </div>
  </div>


</template>

<script>
import SidebarMenu from './SidebarMenu.vue'
import VideoPlayer from './VideoPlayer.vue'
import Chatbot from './Chatbot.vue'
import { marked } from 'marked'

export default {
  name: 'CoursePage',
  components: {
    SidebarMenu,
    VideoPlayer,
    Chatbot
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
      selectedVideoUrl: '',
      summary:'',
      clearHistory:false,
      
    }
  },
  mounted() {
    this.setInitialVideo()
  },
  computed:{
  checkSummary(){
    //console.log(this.summary);
    return this.summary;
  },
  },
  watch: {
    selectedVideoUrl(newValue, oldValue) {
      // This function is called whenever `selectedVideoUrl` changes
      this.getSummary();
      this.clearHistory=true;
      //console.log("selectedVideoUrl:"+this.selectedVideoUrl+this.clearHistory);
    }
  },
  methods: {


    closeChatBot(){
      this.closeSummary();
    },

    closeSummary(){

    this.summary='';

    },


    async getSummary(){
      const response = await fetch(
        `http://127.0.0.1:5000//api/YTSummary?video_url=${this.selectedVideoUrl}`,
        {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        }
      )
      const data = await response.json()
      if (response.ok) {
        this.summary = "explain this lecture " +data['summary']
        //console.log("SUMMARY : "+this.summary)
      } else this.message = data['message']

    },

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
        //console.log(this.weeks_no)
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
