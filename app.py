from flask import Flask, render_template, request

app = Flask(__name__)

modules = {
    1: {
        "title": "Introduction to Security Roles",
        "content": "Security guards maintain safety and enforce rules. Key qualities include observation, communication, and professionalism.",
        "quiz": {
            "What is the primary duty of a security guard?": [
                "Enforce safety", "Break rules", "Ignore incidents"
            ]
        }
    },
    2: {
        "title": "Rules of Engagement",
        "content": "Understand when and how to intervene in various scenarios. Always act within the law.",
        "quiz": {
            "When should a guard intervene?": [
                "Only when trained and safe", "Always", "Never"
            ]
        }
    }
}

@app.route('/')
def home():
    return render_template('home.html', title="Safe Site Security Training")

@app.route('/modules')
def training_modules():
    return render_template('modules.html', modules=modules, title="Training Modules")

@app.route('/module/<int:module_id>')
def module(module_id):
    module = modules.get(module_id)
    return render_template('module.html', module_title=module['title'], 
                           module_content=module['content'], module_quiz=module['quiz'], module_id=module_id)

if __name__ == "__main__":
    app.run(debug=True)
