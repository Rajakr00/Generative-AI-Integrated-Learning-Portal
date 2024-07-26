<template>
    <SidebarMenu :name="course_name" :weeks="weeks_no" />
    <div class="body">
        {{ course_id }} <br>
        {{ user_id }} <br>
        {{ details }} <br>
        {{ weeks_no }} 
    </div>
</template>
    
<script>
    import SidebarMenu from './SidebarMenu.vue';
    export default {    
        name:'CoursePage',
        components: {
            SidebarMenu
        },
        created() {
            this.getCoursesDetails();
        },
        data() {
            return {
                user_id: this.$route.query.user_id,
                course_id: this.$route.query.course_id,
                message:null,
                details:[],
                course_name:null,
                weeks_no:[]
            }
        },
        methods:{
            async getCoursesDetails(){      
                const response = await fetch(`http://127.0.0.1:5000//api/coursePage?user_id=${this.user_id}&course_id=${this.course_id}`, {
                    method: 'GET',
                    headers: {
                    'Content-Type': 'application/json'
                    }
                })
                const data = await response.json();
                if (response.ok) {
                    this.course_name = data['course_name']
                    this.details=data['details']
                    this.weeks_no=Object.entries(this.details).map(([weekNumber,urls]) => ({week: `Week ${weekNumber}`,
                        urls}));
                    console.log(this.weeks_no)
                }
                else
                    this.message=data['message']
            }
        }        
    };
</script>
    
<style scoped>
    .body{
        padding-left:200px;
    }
    
</style>
    