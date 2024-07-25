<template>
  <div class="course-grid">
    <div v-if="no_of_courses==0" style="text-align:center">
      You haven't registered for any courses!
    </div>

    <div v-for="(course, desc) in courses" :key="index" class="course-card">
      <table class="course-details">
        <tr>
          <th class="course-name">{{ course.name }}</th>
        </tr>
        <tr>
          <br>
        </tr>
        <tr>
          <td class="course-desc">{{ course.desc }}</td>
        </tr>
      </table>      
    </div>
  </div>
  </template>
  
  <script>
  export default {
    name:'Dashboard',
    data() {
        return {
            user_id: this.$route.query.user_id,
            courses:[],
            no_of_courses:null,
            response:null
        }
    },
    created() {
        this.getCourses();
    },
    methods:{
      async getCourses(){      
            const response = await fetch(`http://127.0.0.1:5000/api/studentDashboard?user_id=${this.user_id}`, {
                method: 'GET',
                headers: {
                  'Content-Type': 'application/json'
                }
            })
            const data = await response.json();
            if (response.ok) {
                this.courses = data['courses']
                this.no_of_courses=data['no_of_courses']
                console.log(this.response);
            }
            console.log(this.response);
        },
    }
  };
  </script>
  
  <style scoped>
  .course-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(200px, 1fr));
    gap: 16px;
    padding: 16px;
  }
  
  .course-card {
    background-color: #DFD3C3;
    border: 1px solid #8D493A;
    border-radius: 8px;
    padding: 16px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .course-name {
    background-color: #D0B8A8;
    font-size: 27px; 
    color: #973131; 
    font-family: 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    font-weight: bolder;
    padding: 10px;
    text-align: center;
    
  }
  .course-desc {
      background-color: #D0B8A8;
      margin: 100px;
      font-size: 20px; 
      color: #8D493A; 
      font-family:  'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
      font-weight: bolder;
      padding: 10px;
      text-align: center;
  }
  </style>
  