import UIKit
import CocoaMQTT

class ViewController: UIViewController {

    @IBOutlet weak var brightnessPercentage: UILabel!
    @IBOutlet weak var brightnessLabel: UILabel!
    @IBOutlet weak var activityLabel: UILabel!

    //192.168.0.2 is the static IP address of the Raspberry Pi gateway
    var mqttClient = CocoaMQTT(clientID: "iOS Device", host: "192.168.0.2", port: 1883)
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }

    
    @IBAction func connect(_ sender: UIButton) {
        mqttClient.connect()
    }
    
    
    @IBAction func disconnect(_ sender: UIButton) {
        mqttClient.disconnect()
    }
    
    
    @IBAction func refreshBrightness(_ sender: UIButton) {
        mqttClient.publish("connect", withString: "get brightness")
        mqttClient.subscribe("to iOS")
        mqttClient.didReceiveMessage = { mqtt, message, id in
            let brightness = String(Int(message.string!)! * 100 / 256)
            self.brightnessPercentage.text = brightness + "%"
            self.brightnessLabel.text = "Philips Hue: " + (message.string!) + "/256"
        }
    }

    
    @IBAction func refreshActivity(_ sender: UIButton) {
        mqttClient.publish("connect", withString: "get activity")
        mqttClient.subscribe("to iOS")
        mqttClient.didReceiveMessage = { mqtt, message, id in
            self.activityLabel.text = "Activity: " + (message.string!)
        }
    }

}

