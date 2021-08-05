const initialState = {
    shops: [],

};

export default (state=initialState, action) => {
    switch (action.type){
        case 'SET_SHOPS':
            return {
                ...state,
                shops: action.payload
            };
        default:
            return state;
    }
};