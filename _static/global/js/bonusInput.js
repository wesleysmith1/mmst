let bonusInputComponent = {
    props: {
        label: String,
    },
    created: function() {
    },
    data: function() {
        return {
            value: null,
            label: 'yorp yorp'
        }
    },
    methods: {
        submit: function() {
            this.$emit('propose', this.value)
        }
    },
    template:
        `
            <div class="form-inline">
                <div class="form-group">
                    <label for='zzz'>{{label}}\t</label>
                    <input id="zzz" class="form-control mx-sm-3" type="number" v-model="value" placeholder="target">  
                    <button class="btn btn-primary" type="button" @click="submit">submit</button>
                </div>
            </div>
        `
}
