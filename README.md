# Readme

This works on all pi variants, and pings the character 'h' to connected devices.

## Install
```
sudo cp -R ../btkeyboard /usr/local/src/btkeyboard
sudo sh -c "echo 'sudo /usr/local/src/btkeyboard/blues.sh' >> /etc/profile"
```

## To Do

This provides a first implementation for Ubiwrite.

- [x] this will mimic a bluetooth keyboard. It should have an install script, and should operate on boot from both Pi Model Threes and Pi Model Zeros.
- [x] launch on boot across all pi variants, and ping connected devices with a character
- [ ] code for sending arbitrary characters to connected device
- [ ] send characters based on GPIO input patterns
- [ ] shift to a master-slave model, with the left hand modifying the right
- [ ] implement a single charset version of Ubiwrite and test it thoroughly
- [ ] test pwm signal distinction for supporting keyset switching
- [ ] with pwm robustly tested, we will shift to a more generic charset definition model, allowing for easy switching
- [ ] multiple phases of code refactoring will then be necessary - this has been hacky so far, and will only become more grotesque in the near future.
