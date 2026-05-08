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
  const [error, setError] = useState("");
  const navigate = useNavigate();

  // email: 67, name: 6767, password: 67676767

  const submit = async (e) => {
    e.preventDefault();

    if (registerPassword !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/auth/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({"password": registerPassword, "username": registerName})
      });

      if (response.ok) {
        const data = await response.json();
        localStorage.setItem("USER_TOKEN", data.access_token);
        localStorage.setItem("USER_EMAIL", registerEmail);
        navigate("/dashboard");
      } else {
        const text = await response.text();
        // console.log("RAW RESPONSE:", text);

        let message = "User Register Error";
        if (text.includes("<p>")) {
          // extract message from HTML
          const match = text.match(/<p>(.*?)<\/p>/);
          if (match) message = match[1];
        } else {
          try {
            const data = JSON.parse(text);
            message = data.message || data.detail || message;
          } catch {}
        }

        // const errorData = await response.json();
        // console.log(errorData);

        setError(message);
        alert(message);
      }
    } catch (error) {}
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