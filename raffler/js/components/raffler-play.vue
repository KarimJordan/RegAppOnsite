<template>
    <div>
        <div class="container">
            <img id="backgroundimage" :src="raffle_data.background_image" border="0" alt="">
            <center><img class="prize-img" :src="raffle_data.prize_image"></center>
            <div class="raffle-container"></div>
            <button @click="play_raffle" class="raffle-play" id="raffle-play">Iniciar</button>
        </div>
    </div>
</template>
<style>
    @import '~vuejs-noty/dist/vuejs-noty.css';
    #backgroundimage {
        height: auto;
        left: 0;
        margin: 0;
        min-height: 100%;
        min-width: 674px;
        padding: 0;
        position: fixed;
        top: 0;
        width: 100%;
        z-index: -1;
    }
</style>
<script type="text/babel">

    let raffler = require('../external/raffler')
    import axios from 'axios'

    export default {
        name: 'RafflerPlay',
        data() {
            return {
                raffle_data,
                csrf,
                guest_id,
                guestIds: [],
                name_list,
                start_raffle: true
            }
        },
        created() {
            for (let id of this.guest_id) {
                this.guestIds.push(id)
            }
        },
        mounted() {
            let that = this
            let mp3 = require('../assets/raffle.mp3')
            let ogg = require('../assets/raffle.ogg')
            audioPlayer.config({
                files: {
                    mp3: mp3,
                    ogg: ogg
                },
                volume: 0.5
            })

            /** configure raffle controller */
            window.raffle.config({
                names: this.name_list,
                guestIds: this.guestIds,
                container: document.querySelector('.raffle-container'),
                duration: that.raffle_data.draw_duration,
                itemDuration: that.raffle_data.item_duration,
                removeSelected: true
            })

            document.body.onkeyup = function (e) {
                let limit = that.raffle_data.num_of_draws
                let i = 0
                if (e.keyCode == 32) {
                    console.log(that.raffle_data)
                    if (that.raffle_data.num_of_draws == that.raffle_data.num_of_draws_done) {
                        that.$noty.error("Number of draws completed for this raffle.")
                    } else {
                        if (that.start_raffle == true) {
                            window.raffle.play({
                                start: function () {
                                    that.start_raffle = false
                                    audioPlayer.play()
                                },
                                end: function () {
                                    that.start_raffle = true
                                    let lastClass = document.getElementsByClassName('name winner')
                                    let winner_name = lastClass[0].innerText
                                    let winner_id = $('.winner').find('.id').text()

                                    const url = '/rafflers/' + that.raffle_data.id + '/save_winner/'
                                    const method = 'POST'
                                    const redirect = '/raffler/' + this.event_id + '/play_raffle/'

                                    let data = {
                                        'winner_name': winner_name,
                                        'winner_id': winner_id,
                                        'draws': that.raffle_data.num_of_draws_done + 1
                                    }

                                    const request = {
                                        method: method,
                                        url: url,
                                        data: data,
                                        headers: {'X-CSRFToken': this.csrf}
                                    }

                                    axios(request)
                                        .then((response) => {
                                            console.log(response)
                                            that.raffle_data = response.data.raffle
//                                            window.location.replace(redirect);
                                        })
                                        .catch((error) => {
                                            console.log(error)
                                        })

                                }
                            })

                        }
                    }
                }
            }
        },
        methods: {
            play_raffle() {
                window.raffle.play({
                    start: function () {
                        audioPlayer.play()
                    },
                    end: function () {
                        let winner = $('.last').find('.id').text()
                        console.log(winner)
                    }
                })
//                raffle.play({
//                    start: function(){
//                        audioPlayer.play()
//                    },
//                    end: function(){
//                        console.log('lkjlkjlkljlkjkl')
//                    }
//                })
            }
        }
    }
</script>