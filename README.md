Overview of the Application :
This project shows how to design, build, and deploy a web-based Fitness Tracker app in the cloud using modern DevOps methods. The main goal of the project was not only to create a working application, but also to show how Infrastructure as Code (IaC), containerization, and Continuous Integration/Continuous Deployment (CI/CD) can work together in a cloud computing environment.
Users can use the app to keep track of their daily workouts, calories burned, and Body Mass Index (BMI). These features show in a simple but effective way how a dynamic web application can interact with user inputs and give back calculated outputs in real time.

Terraform set up the system's infrastructure by automatically making AWS resources like an EC2 instance, security groups, and IAM roles. This method made sure that infrastructure management could be repeated, scaled up, and version-controlled.

Using Docker, the application was put into containers, which made sure that the runtime environments were the same in both development and production. Amazon Elastic Container Registry (ECR) was used to store the Docker image. It was a secure and central place to keep images.
A GitHub Actions CI/CD pipeline was set up to automate the deployment process. The pipeline automatically builds the Docker image, logs in to Amazon ECR, pushes the image to the registry, and deploys the updated container to the EC2 instance every time code is pushed to the repository. This automated workflow cuts down on the need for people to get involved and makes sure that deployments happen quickly and reliably.

During the development process, there were a number of technical problems, such as setting up IAM permissions for secure ECR access, getting security group rules wrong that affected connectivity, Docker authentication errors, and debugging the CI/CD pipeline. Dealing with these problems made it easier to understand the basics of cloud security, automated deployment strategies, and how to fix problems in distributed systems.

This project shows the whole DevOps lifecycle, from setting up infrastructure to automatically deploying to the cloud. It shows how cloud services, containerization, and automation tools can work together to make a web application solution that can grow and be maintained.
