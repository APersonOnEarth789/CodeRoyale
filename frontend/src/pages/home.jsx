import { FOCUS_CLASS_NAMES } from "@mantine/core";
import Header from "../components/header.jsx";
import styles from "./styles/home.module.css";



const Home = () => {
  return (
    <div className={styles["page"]}>
      <Header isLoggedIn={false} />

      <div className={styles["main"]}>
        <div className={styles["title"]}>Insert home/landing page content here</div>
      </div>
    </div>
  );
}

export default Home;