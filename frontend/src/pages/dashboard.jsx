import Header from "../components/header";
import styles from "./styles/dashboard.module.css";


const Dashboard = () => {
  return (
    <>
      <Header isLoggedIn={true} />

      <div className={styles["main"]}>
        <div className={styles["title"]}>Insert dashboard page content here</div>
      </div>
    </>
  );
};

export default Dashboard;