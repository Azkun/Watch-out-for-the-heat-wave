

// Indev
// Sorry :/

#include <iostream>
#include <thread>
#include <chrono>
class Timer {
    bool clear = false;

    public:
     
        void setInterval(auto function, int interval);
        void stop();

};
void Timer::setInterval(auto function, int interval) {
    this->clear = false;
    std::thread t([=]() {
        while(true) {
            if(this->clear) return;
            std::this_thread::sleep_for(std::chrono::milliseconds(interval));
            if(this->clear) return;
            function();
        }
    });
threehours = 1.08e+7
Timer t = Timer();
t.setInterval([&]() {
    cout << "Please drink water !" << endl;
}, threehours); 
