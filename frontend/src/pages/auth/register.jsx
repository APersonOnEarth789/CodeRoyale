import { useState } from "react";
import { useNavigate, Link, useOutletContext } from "react-router-dom";
import { TextInput, PasswordInput, Button, Title, Paper, Text } from "@mantine/core";
// import errorPopup from "../../helpers/errorPopup";
import styles from "./styles/register.module.css";
import Header from "../../components/header";

const Register = () => {
  const [registerEmail, setRegisterEmail] = useState("");
  const [registerName, setRegisterName] = useState("");
  const [registerPassword, setRegisterPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  // const { users, setUsers } = useOutletContext();
  const navigate = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    navigate("/dashboard");
  }

  const toLandingPage = (e) => {
    e.preventDefault();
    navigate("/");
  };

  return (
    <div>
      <Header />

      <Paper
        shadow="lg"
        radius="md"
        p="xl"
        withBorder
        mx="auto"
        style={{ maxWidth: 400, margin: "40px auto", marginTop: "120px", textAlign: "center" }}
      >
        <Title order={2} mb="md">Register</Title>

        <form onSubmit={submit}>
          <TextInput
            label="Email"
            placeholder="email@example.com"
            value={registerEmail}
            onChange={(e) => setRegisterEmail(e.target.value)}
            required
            mb="sm"
            classNames={{ input: 'input' }}
          />

          <TextInput
            label="Name"
            placeholder="Your Name"
            value={registerName}
            onChange={(e) => setRegisterName(e.target.value)}
            required
            mb="sm"
            classNames={{ input: 'input' }}
          />

          <PasswordInput
            label="Password"
            placeholder="Create Password"
            value={registerPassword}
            onChange={(e) => setRegisterPassword(e.target.value)}
            required
            mb="md"
            classNames={{ input: 'input' }}
          />

          <PasswordInput
            label="Confirm Password"
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
            mb="md"
            classNames={{ input: 'input' }}
            error={registerPassword !== confirmPassword ? "Passwords do not match" : null}
          />

          <Button type="submit" className={styles["submit-button"]}>
            Register
          </Button>
        </form>

        <Text size="sm" mt="md" mb="xl">
          Already have an account?{" "}
          <Link to="/login" className={styles["login-button"]}>
            Login
          </Link>
        </Text>

        <a href="/" className={styles["back-to-landing-page"]}>Back to landing page</a>
      </Paper>
    </div>
  );
}

export default Register;