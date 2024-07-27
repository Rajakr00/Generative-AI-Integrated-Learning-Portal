<template>
  <p class="warning" v-if="message">{{ message }}</p>
  <form @submit.prevent="login">
    Email ID: <input type="text" v-model="username" placeholder="Username" /><br /><br />
    Password : <input type="password" v-model="password" placeholder="Password" />
    <button id="submit" type="submit">Login</button>
  </form>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
      message: null
    }
  },
  methods: {
    async login() {
      const response = await fetch('http://127.0.0.1:5000/api/studentLogin', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password
        })
      })
      const data = await response.json()
      if (response.ok) {
        const user_id = data['user_id']
        this.$router.push({ path: '/studentDashboard', query: { user_id } })
      } else this.message = data['message']
    }
  }
}
</script>

<style scoped>
form {
  font-size: 20px;
  width: 100%;
  align-items: center;
  justify-content: center;
}

fieldset {
  width: fit-content;
  margin: 0 auto;
  width: fit-content;
  padding-top: 40%;
  padding-bottom: 45%;
  font-size: 20px;
  align-items: center;
  justify-content: center;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial,
    sans-serif;
  border: none;
}

legend {
  width: fit-content;
  padding: 3px;
  font-size: 27px;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial,
    sans-serif;
  font-weight: bold;
}

input {
  display: inline-block;
  border: none;
  font-size: 25px;
  margin-left: 20px;
  outline: none;
}

#submit {
  border-radius: 0.2em;
  font-size: 100%;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial,
    sans-serif;
  font-weight: bolder;
  padding: 3%;
  margin-left: 40%;
  margin-top: 10%;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: fit-content;
  cursor: pointer;
  background-color: #8d493a;
  border: none;
}
</style>
