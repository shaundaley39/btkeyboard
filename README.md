# Readme
## 

This provides a first implementation for Ubiwrite.

- [ ] this will mimic a bluetooth keyboard. It should have an install script, and should operate on boot from both Pi Model Threes and Pi Model Zeros.
- [ ] we will implement clients that generate key events through GPIO input patterns. This will be tested across models.
- [ ] we will shift to a master-slave model
- [ ] we will implement a single charset version of Ubiwrite and test it thoroughly
- [ ] we will then seek to test pwm signal distinction for supporting keyset switching
- [ ] with pwm robustly tested, we will shift to a more generic charset definition model, allowing for easy switching
- [ ] multiple phases of code refactoring will then be necessary - this has been hacky so far, and will only become more grotesque in the near future.
