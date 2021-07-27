const initialState = [
    'Technostore',
    'Bershka'
];


export default function  shop(state = initialState, action){
    if (action.type ==='ADD_SHOP'){
    return state;
} else if (action.type ==='DELETE_SHOP'){
    return state;
}
    return state;
}