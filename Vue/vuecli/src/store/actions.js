export default {
    getAddAction(content, data) {
        setTimeout(() => {
            content.commit('getAdd', data)
        }, 1000);

    }
}