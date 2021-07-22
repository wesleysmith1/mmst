let decodeComponent = {
    props: {
        difficult: Boolean,
        numbers: Array,
    },
    created: function() {
        this.generateCode()
    },
    data: function() {
        return {
            userInput: null,
            display: true,

            difficult1: null,
            difficult2: null,
            easy1: null,
            codes: [],
        }
    },
    methods: {
        generateCode: function() {
            if (this.difficult) {
                this.codes = [this.genNum(),this.genNum()]

            } else {
                this.codes = [this.genNum()]
            }
            this.resetInputs()
        },
        decodeSubmit: function() {
            // only submit if there is an input
            if (this.responses.indexOf(null) >= 0) {
                return
            }
            // liveSend it not defined on practice round
            if (typeof liveSend === 'function') {
                liveSend({'codes':this.codes, 'responses': this.responses});
            }
            this.generateCode()
        },
        genNum: function() {
            return this.numbers[Math.floor(Math.random() * this.numbers.length)]
        },
        resetInputs: function() {
            this.easy1 = null
            this.difficult1 = null
            this.difficult2 = null
        }
    },
    computed: {
        responses: function() {
            if (this.difficult) {
                return [this.difficult1, this.difficult2]
            } else {
                return [this.easy1]
            }
        }
    },
    template:
        `
            <div>
                <h3 style="text-align: center;">
                    Code: <span v-for="code in codes">{{code}} </span>
                </h3>
            
                <div v-if="difficult">
                    <div id="difficultForm" class="d-flex justify-content-center">
                        <div class="col-auto">
                            <input type="text" class="form-control mb-2" v-model="difficult1">
                        </div>
                        <div class="col-auto">
                            <input type="text" class="form-control mb-2" v-model="difficult2">
                        </div>
                        <div class="col-auto">
                            <button id="difficultSubmit" type="button" class="btn btn-primary mb-2" @click="decodeSubmit">Submit</button>
                        </div>
                    </div>
                </div>
            
                <div v-if="!difficult">
                    <div class="d-flex justify-content-center">
                        <div class="col-auto">
                            <input type="text" class="form-control mb-2" id="easy" v-model="easy1">
                        </div>
                        <div class="col-auto">
                            <button id="easySubmit" type="button" class="btn btn-primary mb-2" @click="decodeSubmit">Submit</button>
                        </div>
                    </div>
                </div>
            </div>

        `
}
