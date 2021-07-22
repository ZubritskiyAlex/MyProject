import React from "react";
import {BottomNavigation, BottomNavigationAction, makeStyles, Typography} from "@material-ui/core";
import FolderIcon from '@material-ui/icons/Folder'
import RestoreIcon from '@material-ui/icons/Restore'
import FavoriteIcon from '@material-ui/icons/Favorite'
import LocationOnIcon from '@material-ui/icons/LocationOn'

const useStyles = makeStyles((theme) => ({
   root: {
       flexGrow:1
   },
    menuButton: {
       marginRight: theme.spacing(1)
   },
    title: {
       flexGrow:1
    },

    mainFeaturesPost:{
       position: "relative",
       color: theme.palette.common.white,
       marginBottom: theme.spacing(4),
       backgroundSize: "cover",
       backgroundRepeat: "no-repeat",
       backgroundPosition: "center"
    },
    overlay:{
      position: "absolute",
      top: 0,
      bottom: 0,
      right: 0,
      left: 0,
      backgroundOverlay: "rgba(0,0,0.3)"

    },
    mainFeaturesPostContent:{
       position: "relative",
       padding: theme.spacing(6),
       marginTop: theme.spacing(8)
    },
    cardMedia: {
       paddingTop: "56.25%"
    }

}))


function Footer()  {
  const classes = useStyles();
  const [value, setValue] = React.useState("recents")

  const handleChange = (event,newValue) =>{
    setValue(newValue);
  };

    return (


        <footer>
       <Typography variant="h6" align="center" gutterBottom> Footer </Typography>
        <BottomNavigation
            value={value}
            onChange={handleChange}
            className={classes.root}
        >

          <BottomNavigationAction
            label = "Recents"
            value = "recents"
            icon = {<RestoreIcon />}

          />

          <BottomNavigationAction
            label = "Favorites"
            value = "favorites"
            icon = {<FavoriteIcon />}

          />

          <BottomNavigationAction
            label = "Nearby"
            value = "nearby"
            icon = {<LocationOnIcon />}

          />

          <BottomNavigationAction
            label = "Folder"
            value = "recents"
            icon = {<FolderIcon />}

          />
        </BottomNavigation>
        </footer>
    );
}

export default Footer;