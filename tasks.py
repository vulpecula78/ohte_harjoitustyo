from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/mainprg.py")

@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(test)
def coverage_report(ctx):
    ctx.run("coverage report -m")

@task(test)
def coverage_html(ctx):
    ctx.run("coverage html")
