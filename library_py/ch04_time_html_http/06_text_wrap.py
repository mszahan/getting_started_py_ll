import textwrap

webtext = '''   Lorem ipsum dolor sit amet consectetur adipisicing elit. 
Assumenda, cupiditate debitis. Maiores sunt explicabo quaerat rem nostrum 
odit est, suscipit pariatur veritatis dicta, laboriosam earum, 

commodi qui corrupti accusamus eveniet illo ea reprehenderit saepe ipsam. 
Repellat rerum adipisci similique magni!

'''

print('No Dedent---------------------')
print(textwrap.fill(webtext))

print('Dedent-------------------------')
dedent_text = textwrap.dedent(webtext).strip()
print(dedent_text)

print('Fill----------------------------')
print(textwrap.fill(dedent_text, width=50))

print('controlling indent---------------')
print(textwrap.fill(dedent_text, initial_indent='   ', subsequent_indent='  '))

print('Shortening text------------------')
short = textwrap.shorten('LinkedIn learning is ok not so great', width=15, placeholder='...')
print(short)