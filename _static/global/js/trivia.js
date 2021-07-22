let triviaComponent = {
    props: {
        question: null
    },
    created: function() {
    },
    mounted: function() {   
        this.submitTimer()
    },
    data: function() {
        return {
            userInput: null,
            display: true,
            displayBtn: false,
        }
    },
    methods: {
        submitTrivia: function() {
            liveSend({'answer': this.userInput});
            // this.userInput = null
            // this.question = null
            this.display = false
            this.displayBtn = false
        },
        submitTimer: function() {
            // display submit button
            setTimeout(() => {this.displayBtn = true}, 15000)
        },
    },
    watch: {
        question: function(val) {
            if (val) {
                
                setTimeout(() => {this.display = true}, 1000)
                this.submitTimer()
            }
        }
    },
    template:
        `
            <div>
                 <form v-if="display" @submit.prevent="submitTrivia">
                    <div class="form-group required">
                        <div>{{question.question}}</div>

                        <div class="form-check" v-for="(option, index) in question.options">
                            <input class="form-check-input" type="radio" name="flexRadioDefault" :id="'radio' + index" :value="option" @input="userInput = option" required="">
                            <label class="form-check-label" :for="'radio' + index">
                                {{option}}
                            </label>
                        </div>
                        <br>
                        <button v-if="displayBtn" class="btn btn-primary" type="submit">Submit</button>
                    </div>
                </form>

            </div>

        `
}
