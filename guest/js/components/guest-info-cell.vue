<template>
    <div class="row">
      <ul class="list-unstyled">
        <li class="panel" v-for="(field, index) in items">
          <div class="panel-body">
            <div class="col-md-7 col-sm-7">
                <input v-model="input_val[index]" @input="changed(index, input_val[index])" type="text"
                       class="form-control" :placeholder="field.field_name"/>
            </div>
            <div class="col-md-5">
            </div>

          </div>
        </li>
      </ul>
    </div>
</template>
<script type="text/babel">
    export default {
        name: 'GuestInfoCell',
        props: {
            items: {
                type: Array,
                required: true
            }
        },
        data() {
            return {
                input_val: [],
                guest_list: [],
                guest_data: {
                    order: '',
                    event_id: '',
                    field_name: '',
                    id: '',
                    is_email: '',
                    is_required: '',
                    is_resolved: '',
                    is_unique: '',
                    key: '',
                    value: ''
                }
            }
        },
        watch: {
            input_val: function (val) {
                this.input_val = val
            }
        },
        created() {
              for(const field of this.items){
                  let guest_data = {
                      order: field.order,
                      event_id: field.event_id,
                      field_name: field.field_name,
                      id: field.id,
                      is_email: field.is_email,
                      is_required: field.is_required,
                      is_unique: field.is_unique,
                      key: field.field_name,
                      value: ''
                  }
                  this.guest_list.push(guest_data)
                  this.input_val.push('')
              }
        },
        methods: {
            changed(index, val){
                this.input_val[index] = val
                this.guest_list[index].value = this.input_val[index]
                this.$emit('input', this.guest_list)
            },
        }

    }
</script>