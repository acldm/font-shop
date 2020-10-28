window.addEventListener('load', function() {
  window.app = new Vue({
    el: "#app",
    data: {
      msg: "hello",
      username: "",
      password: "",
      num: 20
    },
    computed: {
      test() {
        return "hello"
      }
    },
    created() {
      console.log(this.msg);
    }
  })
})
