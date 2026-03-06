from flask import Flask, redirect, request, render_template
from proguin.core import load_pages_default, save_pages_default

app = Flask(__name__)


def get_current_page(pages):
    page_id = pages.get("current_page", "default")
    page = pages.get("pages", {}).get(page_id, {"title": page_id, "tasks": []})
    tasks = page.get("tasks", [])
    return page_id, page, tasks


@app.route("/")
def home():
    pages = load_pages_default()
    page_id, page, tasks = get_current_page(pages)

    return render_template(
        "index.html",
        tasks=tasks,
        page_title=page.get("title", page_id)
    )


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/add", methods=["POST"])
def add_task():
    pages = load_pages_default()
    page_id, page, tasks = get_current_page(pages)

    name = request.form.get("task_name", "").strip()

    if name:
        tasks.append({
            "name": name,
            "completed": False
        })
        save_pages_default(pages)

    return redirect("/")


@app.route("/done/<int:index>")
def mark_done(index):
    pages = load_pages_default()
    page_id, page, tasks = get_current_page(pages)

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = not tasks[index].get("completed", False)
        save_pages_default(pages)

    return redirect("/")


@app.route("/delete/<int:index>")
def delete_task(index):
    pages = load_pages_default()
    page_id, page, tasks = get_current_page(pages)

    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_pages_default(pages)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)