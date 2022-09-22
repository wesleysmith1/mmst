let bonusInputComponent = {
    props: {
        label: String,
    },
    created: function() {
    },
    data: function() {
        return {
            value: null,
        }
    },
    methods: {
        submit: function() {
            if (this.value)
                this.$emit('propose', this.value)
        },
        isNumber: function(evt) {
            evt = (evt) ? evt : window.event;
            var charCode = (evt.which) ? evt.which : evt.keyCode;
            if ((charCode > 31 && (charCode < 48 || charCode > 57)) && charCode !== 46) {
              evt.preventDefault();;
            } else {
              return true;
            }
          }
    },
    template:
        `
            <div>

                <div class="row g-3 align-items-center">
                    <div class="col-auto">
                        <label class="col-form-label" for="targetInput">{{label}}</label>
                    </div>
                    <div class="col-auto">
                        <input id="targetInput" type="number" @keypress="isNumber($event)" @click="submit" class="form-control" v-model="value" name="target" placeholder="target">    
                    </div>
                    <div class="col-auto">
                        <button class="btn btn-primary" type="button" @click="submit">submit</button>
                    </div>
                </div>
            </div>
        `
}