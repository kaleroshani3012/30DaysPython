import argparse

def cel_to_far(c):
    return (c* 9/5) + 32

def far_to_cel(f):
    return (f-32) * 5/9

parser = argparse.ArgumentParser(description= "Temprature Converter CLI Tool")

parser.add_argument("temperature", type = float, help= "Temperature value to convert")
parser.add_argument(
    "--to",
    choices = ["celsius", "fahrenheit"],
    required=True,
    help="Convert to 'celsius' or 'fahrenheit'",
)

args = parser.parse_args()

if args.to == "fahrenheit":
    result = cel_to_far(args.temperature)
    print(f"{args.temperature}°C is {result:.2f}°F")
elif args.to == "celsius":
    result = far_to_cel(args.temperature)
    print(f"{args.temperature}°F is {result:.2f}°C")