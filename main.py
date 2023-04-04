import argparse

# 创建 ArgumentParser 对象并定义父命令参数
parser = argparse.ArgumentParser(description='My program')
parser.add_argument('--verbose', action='store_true', help='enable verbose mode')

# 定义子命令及其参数
subparsers = parser.add_subparsers(help='sub-command help')

# 子命令1x
parser_cmd1 = subparsers.add_parser('cmd1', help='command 1 help')
parser_cmd1.add_argument('-a', '--arg', type=str, help='argument 1 for command 1')
parser_cmd1.set_defaults(command='cmd1')

# 子命令2
parser_cmd2 = subparsers.add_parser('cmd2', help='command 2 help')
parser_cmd2.add_argument('-a', '--arg', type=str, help='argument 1 for command 1')
parser_cmd2.set_defaults(command='cmd2')

# 解析命令行参数
args = parser.parse_args()

# 判断用户选择的子命令
if args:
    if args.command == 'cmd1':
        print('command 1')
        print(args.arg)
    elif args.command == 'cmd2':
        print('command 2')
        if args.verbose:
            print('verbose mode')
        else:
            print(args.arg)
