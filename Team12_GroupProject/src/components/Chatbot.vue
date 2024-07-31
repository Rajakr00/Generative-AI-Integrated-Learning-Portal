<template>
    <div class="container m-4">
        <div class="card mx-auto">
            <div class="card-header bg-transparent">
                <div class="navbar navbar-expand p-0">
                    <h5>Chatbot</h5>
                </div>
            </div>
            <div class="card-body p-4" style="height: 400px; overflow: auto;">

                <div class="d-flex align-items-baseline mb-4">
                    <div class="position-relative avatar">
                        <img src="https://s.yimg.com/ny/api/res/1.2/zWHycYRsBKQ6xwdBGQtw4g--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTU0MDtjZj13ZWJw/https://s.yimg.com/os/creatr-uploaded-images/2023-12/5f7be670-943f-11ee-af7f-41b7060d20ba"
                            class="img-fluid" style="border-radius: 50%; height:100%;" alt="">
                        <span
                            class="position-absolute bottom-0 start-100 translate-middle p-1 bg-success border border-light rounded-circle">
                            <span class="visually-hidden">New alerts</span>
                        </span>
                    </div>
                    <div class="pe-2">
                        <div>
                            <div class="card card-text d-inline-block p-2 px-3 m-1">Hi! How may i assist you today?
                            </div>
                        </div>
                        
                    </div>
                </div>


                <!--
                <div class="d-flex align-items-baseline text-end justify-content-end mb-4">
                    <div class="pe-2">
                        <div>
                            <div class="card card-text d-inline-block p-2 px-3 m-1">Sure</div>
                        </div>
                        <div>
                            <div class="card card-text d-inline-block p-2 px-3 m-1">Let me know when you're available?
                            </div>
                        </div>
                        <div>
                            <div class="small">01:13PM</div>
                        </div>
                    </div>
                    <div class="position-relative avatar">
                        <img src="https://nextbootstrap.netlify.app/assets/images/profiles/2.jpg"
                            class="img-fluid rounded-circle" alt="">
                        <span
                            class="position-absolute bottom-0 start-100 translate-middle p-1 bg-success border border-light rounded-circle">
                            <span class="visually-hidden">New alerts</span>
                        </span>
                    </div>
                </div>

                <div class="d-flex align-items-baseline mb-4">
                    <div class="position-relative avatar">
                        <img src="https://nextbootstrap.netlify.app/assets/images/profiles/1.jpg"
                            class="img-fluid rounded-circle" alt="">
                        <span
                            class="position-absolute bottom-0 start-100 translate-middle p-1 bg-success border border-light rounded-circle">
                            <span class="visually-hidden">New alerts</span>
                        </span>
                    </div>
                    <div class="pe-2">
                        <div>
                            <div class="card card-text d-inline-block p-2 px-3 m-1">3:00pm??</div>
                        </div>
                        <div>
                            <div class="small">Edited - 01:13PM</div>
                        </div>
                    </div>
                </div>

                <div class="d-flex align-items-baseline text-end justify-content-end mb-4">
                    <div class="pe-2">
                        <div>
                            <div class="card card-text d-inline-block p-2 px-3 m-1">Cool</div>
                        </div>
                        <div>
                            <div class="card card-text p-2 px-3 m-1 mb-5">
                                <div class="row align-items-center">
                                    <div class="col-1">
                                        <a href=""><i class="fas fa-play"></i></a>
                                    </div>
                                    <div class="col">
                                        <div class="progress" style="width:100px; height: 4px;">
                                            <div class="progress-bar bg-primary" role="progressbar" style="width: 35%"
                                                aria-valuenow="35" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </div>
                                    <div class="col-auto">
                                        <div class="small fw-bold">0:34</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="position-relative avatar">
                        <img src="https://nextbootstrap.netlify.app/assets/images/profiles/2.jpg"
                            class="img-fluid rounded-circle" alt="">
                        <span
                            class="position-absolute bottom-0 start-100 translate-middle p-1 bg-success border border-light rounded-circle">
                            <span class="visually-hidden">New alerts</span>
                        </span>
                    </div>
                </div>
            
            -->
            <div class="messages-container">
              <div v-for="(msg, index) in messages" :key="index" :class="{'justify-content-end': msg.sender === 'me', 'justify-content-start': msg.sender !== 'me'}" class="d-flex align-items-baseline mb-4">
                <div v-if="msg.sender === 'me'" class="d-flex">
                <div class="pe-2">
                  <div>
                    <div class="card card-text d-inline-block p-2 px-3 m-1" v-html="msg.text"></div>
                  </div>
                </div>

                <div>
                    <div class="position-relative avatar">
                        <i class="bx bx-user bx-md"></i>
                        <span
                            class="position-absolute bottom-0 start-100 translate-middle p-1 bg-success border border-light rounded-circle">
                            <span class="visually-hidden">New alerts</span>
                        </span>
                    </div>

                  </div>
                </div>
            
                <div v-else class="d-flex">

                    <div>
                    <div class="position-relative avatar">
                        <img src="https://s.yimg.com/ny/api/res/1.2/zWHycYRsBKQ6xwdBGQtw4g--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTU0MDtjZj13ZWJw/https://s.yimg.com/os/creatr-uploaded-images/2023-12/5f7be670-943f-11ee-af7f-41b7060d20ba"
                            class="img-fluid" style="border-radius: 50%; height:100%;" alt="">
                        <span
                            class="position-absolute bottom-0 start-100 translate-middle p-1 bg-success border border-light rounded-circle">
                            <span class="visually-hidden">New alerts</span>
                        </span>
                    </div>

                  </div>

                <div class="pe-2">
                  <div>
                    <div class="card card-text d-inline-block p-2 px-3 m-1" v-html="msg.text"></div>
                  </div>
                </div>
            </div>
            </div>
          </div>
            </div>
        


             <!-- card-body end -->
            <div class="m-5"></div>

            <div class="card-footer bg-white position-absolute w-100 bottom-0 m-0 p-1">
                <div class="input-group">
                    <div class="input-group-text bg-transparent border-0">
                        <button class="btn btn-light text-secondary">
                            <i class="bx bx-paperclip bx-sm"></i>
                        </button>
                    </div>
                    <input type="text" v-model="message" class="form-control border-0" placeholder="Write a message..." @keyup.enter="sendMessage(message,'me')">
                    <div class="input-group-text bg-transparent border-0" >
                        <button @click="sendMessage(message,'me')" class="btn btn-light text-secondary">
                            <i class="bx bx-send bx-sm"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
  name: 'Chatbot',
  data() {
    return {
      message:'',
      messages:[],
    }
  },
  created() {
    this.getCourses()
  },
  methods: {


    async sendMessage(text, sender) {
      if (text.trim()) {

        this.messages.push({ text: text, sender: sender });  // add the message with sender information to the array
        this.message = '';  // clear the input field after sending the message

        const response = await fetch(
        `http://127.0.0.1:5000/api/Chat?query=${text}`,
        {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        }
      )
      const data = await response.json()
      if (response.ok) {
        this.receiveMessage(data['message']);
      }

      }
    },

    receiveMessage(text) {
      if (text.trim()) {
        this.messages.push({ text: text, sender: 'other' });  // add the message from the other user to the array
      }
    },

    async getCourses() {
      const response = await fetch(
        `http://127.0.0.1:5000/api/studentDashboard?user_id=${this.user_id}`,
        {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        }
      )
      const data = await response.json()
      if (response.ok) {
        this.courses = data['courses']
        this.no_of_courses = data['no_of_courses']
      }
    },
    redirectCoursePage(course_id) {
      console.log('Redirecting to course ID:', course_id)
      this.$router.push({
        path: '/coursePage',
        query: { course_id: course_id, user_id: this.user_id }
      })
    }
  }
}
</script>


<style>
    a.nav-link {
        color: gray;
        font-size: 18px;
        padding: 0;
    }

    .avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        border: 2px solid #b09a95;
        padding: 2px;
        flex: none;
    }

    input:focus {
        outline: 0px !important;
        box-shadow: none !important;
    }

    
</style>